from odoo import fields, models


class StopAction(models.Model):
    _name = "stop.action"
    _description = "Stop Action"
    _order = "id desc"
    
    _sql_constraints = [
        ("check_unique_cron_id", "UNIQUE(cron_id)", "Scheduled Actions already added!"),
    ]

    cron_id = fields.Many2one("ir.cron", string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)