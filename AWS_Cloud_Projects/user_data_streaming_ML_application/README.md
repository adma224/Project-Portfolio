AWS-UserDataStreamingMLApplication/
├── cloudformation/                         # CloudFormation related files
│   ├── templates/                          # CloudFormation templates
│   │   └── user-data-producer.json         # Additional CloudFormation template for user data
│   └── images/                             # Diagrams and images related to CloudFormation
│       └── cloud_formation_template.png
├── src/                                    # Source code for the application
│   ├── ec2/                                # Scripts related to EC2 setup
│   │   └── ec2_instance_create.py          # Script to create EC2 instances
│   ├── iam/                                # IAM-related scripts
│   │   └── iam_ec2_role_create.py          # Script to create IAM roles for EC2
│   ├── kinesis/                            # Kinesis service setup scripts
│   │   ├── kinesis_analytics_set_up.py     # Set up Kinesis Analytics
│   │   ├── kinesis_firehose_create.py      # Create Kinesis Firehose delivery stream
│   │   └── kinesis_stream_create.py        # Script to create a Kinesis stream
│   ├── lambda/                             # Lambda function scripts
│   │   └── transform_lambda_function.py    # Lambda function for data transformation
│   ├── s3/                                 # Scripts for S3 bucket operations
│   │   └── s3_bucket_create.py             # Script to create an S3 bucket
│   └── tests/                              # Tests for the resources
│       └── test_for_resources.py           # Unit tests for the application resources
├── config/                                 # Configuration files
│   └── variables.env                       # Environment variables and configurations
├── docs/                                   # Documentation files
│   └── design_narrative.pdf                # Detailed design narrative of the project
├── README.md                               # Project overview and setup instructions
├── .gitignore                              # Specifies intentionally untracked files to ignore
└── requirements.txt                        # Python dependencies for the project
