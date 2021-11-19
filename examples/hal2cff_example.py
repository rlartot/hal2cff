from hal2cff import hal2cff
import ipywidgets as widgets
from IPython.display import display, display_html, Markdown

# # hal2cff example


print(hal2cff("https://hal.archives-ouvertes.fr/hal-01361430v1"))

#SETUP all UI
query=widgets.Textarea(
    value='https://hal.archives-ouvertes.fr/hal-01361430v1'
)
button = widgets.Button(description="Let's roll on")

#render everything
display(widgets.HBox([query, button]))

output = widgets.Output()


def run_and_display_query(_):
    result = hal2cff(query.value)
    return result


button.on_click(run_and_display_query)
run_and_display_query(None)

output


