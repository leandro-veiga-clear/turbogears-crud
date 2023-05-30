# -*- coding: utf-8 -*-
"""Product controller module"""

from tg import expose, redirect, validate, flash, url
# from tg.i18n import ugettext as _
# from tg import predicates

from crud.lib.base import BaseController
from crud.model import DBSession, Product

class ProductController(BaseController):
    # Uncomment this line if your controller requires an authenticated user
    # allow_only = predicates.not_anonymous()

    @expose('crud.templates.products_list')
    def index(self, **kw):
        products = DBSession.query(Product).all()
        return dict(page='product-index', products=products)

    @expose('crud.templates.products_form')
    def new(self, **kw):
        return dict(page='product-new', product=None, button_label='new')
    
    @expose('crud.templates.products_form')
    def edit(self, id):
        product = DBSession.query(Product).get(id)
        return dict(page='product-edit', product=product, button_label='edit')
    
    @expose()
    def save(self, **kw):   
        if 'id' not in kw:
            product = Product(name=kw['name'], price=kw['price'])
            DBSession.add(product)
        else:
            product = DBSession.query(Product).get(kw['id'])
            product.name = kw['name']
            product.price = kw['price']
        redirect('/' + 'product')

    @expose()
    def delete(self, id):   
        product = DBSession.query(Product).get(id)
        DBSession.delete(product)
        redirect('/' + 'product')
