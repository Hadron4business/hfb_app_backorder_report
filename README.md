# Backorder Report for Customers

Scheduled e-mail to each customer listing the products not delivered yet, with the planned date.

## What it does

- **Automatic** - Sent on a schedule (weekly by default, adjustable). Customers with nothing pending get nothing.
- **One e-mail per customer** - All open deliveries of the customer and of its contacts in one table: order, product, quantity, planned date, status.
- **Editable template** - The e-mail is a standard Odoo template - change the text, translate it, add your branding.
- **Opt-out per customer** - Tick No Backorder Report on a customer to stop the e-mails.
- **Manual sending** - Send the report to one customer at any time from the Action menu of the contact.
- **Logged** - Each sending is noted in the customer's chatter.

## How to use it

1. Go to Inventory > Configuration > Settings, section Operations, and tick Send Backorder Reports to Customers. The Schedule link opens the scheduled action (frequency, next run).
2. Optionally, on a customer (tab Sales & Purchase, section Misc), tick No Backorder Report.
3. To try it, open a customer with open deliveries and use Action > Send Backorder Report.
4. The scheduled action then e-mails every customer with products not delivered yet.

## Good to know

- Not delivered yet = outgoing stock moves that are neither done nor cancelled (waiting for stock or being prepared).
- The e-mail goes to the company contact of the customer, so it needs an e-mail address.
- Multi-company: each company enables the report separately.

## Technical

- Depends only on `stock`.
- Scheduled action `Backorder Report: e-mail customers` -> `res.partner._cron_send_backorder_report()`.
- Template `hfb_app_backorder_report.mail_template_backorder_report` (lines from `res.partner.get_backorder_report_lines()`).

## Status

Odoo 20 build. Tested on the Odoo.sh test instances (automated RPC tests and manual tests, 2026-10-09). Missing before publication: icon, banner.
