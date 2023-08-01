import data_analytics
import panel as pn


def update_pages(event):
    """Callback function that will update the graphs with new input

    :param event: Unused.
    """
    global tabs, data_analyser
    data_analyser.update_dataframe()
    tabs[0] = ("Main", pn.Column(data_analyser.view_main()))
    tabs[1] = ("Salary Info", pn.Column(data_analyser.view_salary_info()))
    tabs[2] = ("Interest Info", pn.Column(data_analyser.view_interest_info()))


if __name__ == '__main__':
    data_analyser = data_analytics.DataAnalysis()
    data_analyser.set_update(update_pages)
    tabs = pn.Tabs(
        ("Main", pn.Column(data_analyser.view_main())),
        ("Salary Info", pn.Column(data_analyser.view_salary_info())),
        ("Interest Info", pn.Column(data_analyser.view_interest_info())),
        dynamic=True
    )
    template = pn.template.FastListTemplate(title="Financial Toolkit", sidebar=data_analyser.return_sidebar(),
                                            main=tabs)
    template.servable()
    template.show()
