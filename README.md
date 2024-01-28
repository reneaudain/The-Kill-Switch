# The Kill Switch

## Project Overview

"The Kill Switch" is a Python-based tool that automates the shutdown of AWS EC2 instances across a region, filtering by specific department tags. The project integrates with AWS API Gateway, allowing users to trigger the shutdown process via a POST method, passing the relevant tags directly to the script.

## Features

- **Automated EC2 Shutdown**: Efficiently locates and shuts down EC2 instances in a specified AWS region.
- **Tag-Based Filtering**: Targets instances based on department-specific tags, enabling precise control over which instances are affected.
- **API Gateway Integration**: Leverages AWS API Gateway for initiating the shutdown process, making it accessible and manageable remotely.
- **Scalability and Security**: Designed with cloud best practices in mind, ensuring scalability and security.

## Getting Started

### Prerequisites

- AWS account with access to EC2, Lambda, and API Gateway.
- Python environment for script execution.
- Necessary permissions to manage EC2 instances and set up API Gateway and Lambda functions.

### Installation and Usage

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/reneaudain/the-kill-switch.git
2. Set Up AWS Credentials:
   Configure your AWS credentials using the AWS CLI or environment variables.

3. Deploy the Script:
   Follow the included instructions to deploy the script in your AWS environment.

4. Trigger Shutdown via API Gateway:
   Use the provided API Gateway endpoint to send a POST request with the required department tag.

### Hello Beautiful People!

[![Linkedin Badge](https://img.shields.io/badge/-Rene%20Audain-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/rene-audain/)](https://www.linkedin.com/in/rene-audain/)
[![Medium Badge](https://img.shields.io/badge/Rene%20Audain-12100E?style=flat-square&logo=medium&logoColor=white&link=https://medium.com/@rene.audain)](https://medium.com/@rene.audain)
[![Gmail Badge](https://img.shields.io/badge/-rene.audain@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:rene.audain@gmail.com)](mailto:rene.audain@gmail.com)

## ⚡ Technologies

![Amazon AWS](https://img.shields.io/badge/Amazon%20AWS-232F3E?style=flat-square&logo=amazon-aws)
![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
![API Gateway](https://img.shields.io/badge/API%20Gateway-1E1E1E?style=flat-square&logo=amazonaws&logoColor=white)
![Lambda](https://img.shields.io/badge/Lambda-FF9900?style=flat-square&logo=awslambda&logoColor=white)

Contributing
Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

