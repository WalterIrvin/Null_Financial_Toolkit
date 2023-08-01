import data_analytics
import panel as pn


if __name__ == '__main__':
    data_analyser = data_analytics.DataAnalysis()
    tabs = pn.Tabs(
        ("Main", pn.Column(data_analyser.view_main())),
        ("Salary Info", pn.Column(data_analyser.view_salary_info())),
        ("Interest Table", pn.Column(data_analyser.view_interest_info())),
        dynamic=True
    )
    template = pn.template.FastListTemplate(title="Financial Toolkit", sidebar=data_analyser.return_sidebar(),
                                            main=tabs)
    template.servable()
    template.show()
