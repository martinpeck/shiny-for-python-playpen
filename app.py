from shiny import App, render, ui
from matplotlib import pyplot as plt
from random import randint

app_ui = ui.page_fluid(
    ui.h2("This is pretty cool!"),
    ui.input_slider("x", "Number", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.output_plot("a_scatter_plot"),
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"x*2 is {input.x() * 2}"
    
    @output
    @render.plot
    def a_scatter_plot():
        return plt.scatter([1,2,3,4], [randint(0,100),
                                       randint(0,100), 
                                       randint(0,100), 
                                       input.x()])

app = App(app_ui, server)
