from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    """
    Function to desplay Error page
    """
    return render_template('four_Ow_four.html'),404