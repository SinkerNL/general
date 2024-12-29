# Build a simple s3 bucket with terraform
In this example I just build a very simple s3 website. It's not more then just creating the S3 bucket and put an index.html in front of it.

Just for fun, if you want to know the website name afterward, just type in: 

```
terraform state show aws_s3_bucket_website_configuration.static_website
```

Here you will see the website_endpoint for the open stuff. 