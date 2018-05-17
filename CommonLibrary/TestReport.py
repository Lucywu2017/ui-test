# -*- coding: utf-8 -*-

import os
import lxml.etree as my_tree
from lxml import html
from CommonLibrary.CommonConfiguration import result_path


class TestReport(object):

    """description of class"""
    def __init__(self, test_case_info):
        self.test_case_info = test_case_info
        self.report_file = result_path() + r'\TestResult.html'

    # Create init test report file
    def create_html_file(self):
        if not os.path.exists(self.report_file):
            f = open(self.report_file, 'w')
            message = """
            <html>
               <head>    
                    <title>Automation Test Result</title>
                    <style>
                        table {
                                border-collapse: collapse;
                                padding: 15px;
                                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                                }
                        th{
                            background-color: green;
                            color: white;
                            border: 1px solid #ddd;
                            padding-bottom: 15px;
                            padding-top: 15px;
                        }
                        tr{
                            border: 1px solid #008000;
                            padding-bottom: 8px;
                            padding-top: 8px;
                            text-align: left;
                        }
                        td{
                            border: 1px solid #008000;
                        } 
                    </style>
                </head>
                <body>
                    <h1>Automation Test Result</h1>
                    <table>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Author</th>
                            <th>Result</th>
                            <th>StartTime</th>
                            <th>EndTime</th>
                            <th>Duration(s)</th>
                            <th>ErrorInfo</th>
                       </tr>
                    </table>
                </body>
            </html>
            """
            f.write(message)
            f.close()

    def write_html(self,):
        self.create_html_file()

        f = open(self.report_file, "r")

        html_content = f.read()
        f.close()
        html_content.encode('utf-8')
        tree = html.fromstring(html_content)
        tableElem = tree.find(".//table")
        # format = tuple([v for v in self.testcaseinfo.__dict__.values()])

        if self.test_case_info.result == "Failed":
            my_table_row = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td bgcolor=\"#FF0000\">{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td></tr>".format(
                self.test_case_info.id, self.test_case_info.name, self.test_case_info.author, self.test_case_info.result, self.test_case_info.start_time,
                self.test_case_info.end_time, self.test_case_info.seconds_duration, self.test_case_info.error_info)
        else:
            my_table_row = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td></tr>".format(
                self.test_case_info.id, self.test_case_info.name, self.test_case_info.author, self.test_case_info.result, self.test_case_info.start_time,
                self.test_case_info.end_time, self.test_case_info.seconds_duration, self.test_case_info.error_info)
        tableElem.append(my_tree.HTML(str(my_table_row)))

        f = open(self.report_file, "w")
        # html.tostring
        newContent = repr(html.tostring(tree, method="html", with_tail=False))
        newContent = newContent.replace(r"\n", "").replace(r"\t", "").replace('b\'', "").replace('\'', '')
        newContent = newContent[:len(newContent) - 1]
        f.write(newContent)
        f.close()




