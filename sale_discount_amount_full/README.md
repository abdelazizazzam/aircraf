Module: sale_discount_amount_full (Odoo 18)
-------------------------------------------
This addon adds a `discount_amount` float field on sale.order.line and account.move.line,
and provides a POS helper JS method `set_discount_amount(amount)` to set discount as fixed amount.

Notes:
- To display the discount_amount field in forms/tree views, either use Odoo Studio or add view XML.
- The implementation converts discount_amount to the existing `discount` percentage field automatically.
- Test in staging before production.

How to show fields in views (example XML snippet you can adapt):
<odoo>
  <record id="sale_order_line_form_inherit" model="ir.ui.view">
    <field name="name">sale.order.line.form.discount.amount</field>
    <field name="model">sale.order.line</field>
    <field name="inherit_id" ref="sale.view_order_form"/>
    <field name="arch" type="xml">
      <xpath expr="//field[@name='order_line']/form//field[@name='discount']" position="after">
        <field name="discount_amount"/>
      </xpath>
      <xpath expr="//field[@name='order_line']/tree//field[@name='discount']" position="after">
        <field name="discount_amount"/>
      </xpath>
    </field>
  </record>
</odoo>
