import data_analytics
import panel as pn


if __name__ == '__main__':
    data_analyser = data_analytics.DataAnalysis()
    tabs = pn.Tabs(
        ("Main", pn.Column("Example text here.")),
        ("Salary Info", pn.Column("WIP")),
        ("Interest Table", pn.Column("WIP")),
        dynamic=True
    )
    template = pn.template.FastListTemplate(title="Financial Toolkit", sidebar=data_analyser.return_sidebar(),
                                            main=tabs)
    template.servable()
    template.show()
