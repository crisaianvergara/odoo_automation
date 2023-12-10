from odoo import models

import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _get_cron_id(self, cron_id):
        cron = self.env["stop.action"].search([
            ("cron_id", "=", cron_id),
            ("active", "=", True),
        ], limit=1)
        
        return cron

    def _auto_delete_contacts(self, contact_contains_word=None, limit=None, cron_id=None):
        _logger.info('function: _auto_delete_contacts')
        _logger.info(f'contact_contains_word: {contact_contains_word}, limit: {limit}')
        _logger.info(f'Scheduled Action ID: {cron_id}')

        domain = [("name", "ilike", contact_contains_word)]
        for_deletion = self.search(domain, limit=limit)

        if self._get_cron_id(cron_id):
            if for_deletion.exists():
                for_deletion.unlink()

                _logger.info("-----")
                _logger.info("Contact:: For Deletion: %s" % for_deletion)
                _logger.info("-----")
        else:
            _logger.info("-----")
            _logger.info("Delete Contact Failed!")
            _logger.info("-----")

    def _auto_create_contacts(self, limit=None, cron_id=None):
        _logger.info('function: _auto_create_contacts')
        _logger.info(f'limit: {limit}')
        _logger.info(f'Scheduled Action ID: {cron_id}')
        
        if self._get_cron_id(cron_id):
            for i in range(0, limit):
                self.create({'name': 'PyVer Community User - ' + str(i)})

                _logger.info("-----")
                _logger.info("Contact:: Created: %s" % i)
                _logger.info("-----")
        else:
            _logger.info("-----")
            _logger.info("Create Contact Failed!")
            _logger.info("-----")