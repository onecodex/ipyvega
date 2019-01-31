from __future__ import absolute_import

from .base import VegaBase


class Vega(VegaBase):
    """Display a Vega visualization in the Jupyter Notebook."""

    render_type = 'vega'


def entry_point_renderer(spec, embed_options=None):
    vl = Vega(spec, opt=embed_options)
    return vl._repr_mimebundle_()


__all__ = ['Vega', 'entry_point_renderer']
