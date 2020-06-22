import requests
import json
from mail import MailApprove

# Class to approve request
class ApproveResignation():
    
    # constructor for Class
    def __init__(self):
        self.request_link="https://eashanjindal.github.io/SE-Assignment/emp_data.json"
        self.response=json.loads(requests.get(self.request_link).text)

    def approve(self):

        # Approving request
        if(self.response["status"]=="Not Approved"):
            {
                print(self.response["name"], self.response["designation"])
                # print(self.response["status"]="Approved")
                MailApprove()

                    
            }

test1 = ApproveResignation()
print(test1.approve())