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
    
    @expose('crud.templates.list_products')
    def index(self, **kw):
        products = DBSession.query(Product).all()
        return dict(page='product-index', data=[product for product in products])
