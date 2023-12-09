from odoo import models

import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _auto_delete_contacts(self, contact_contains_word=None, limit=None):
        _logger.info('function: _auto_delete_contacts')
        _logger.info(f'contact_contains_word: {contact_contains_word}, limit: {limit}')

        domain = [("name", "ilike", contact_contains_word)]
        for_deletion = self.search(domain, limit=limit)

        if for_deletion.exists():
            for_deletion.unlink()

    def _auto_create_contacts(self, limit=None):
        _logger.info('function: _auto_create_contacts')
        _logger.info(f'limit: {limit}')

        for i in range(0, limit):
            self.create({'name': 'PyVer Community User - ' + str(i)})
