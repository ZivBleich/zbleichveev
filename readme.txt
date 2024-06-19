docker build -t myimage . ; docker run -it -p 8080:8080 myimage

### Examples:
# create a user

Request:
> POST /v1/users HTTP/1.1
> Host: localhost:8080
> Content-Type: application/json
> Accept: */*
> Content-Length: 65

| {"name": "ziv", "email": "ziv@gmail.com", "password": "12345678"}

Response:
{
	"message": {
		"_id": "6672ec0cb6512777d43330f2",
		"email": "ziv@gmail.com",
		"name": "ziv",
		"password": "12345678"
	}
}
200

# list users
Request:
> GET /v1/users HTTP/1.1
> Host: localhost:8080
> Accept: */*

Response:
200
{
	"message": [
		{
			"_id": "6672eb7ab6512777d43330f1",
			"email": "ziv@gmail.com",
			"name": "ziv",
			"password": "12345678"
		}
	]
}
# update a user
Request:
> PATCH /v1/users/6672eb7ab6512777d43330f1 HTTP/1.1
> Host: 127.0.0.1:8080
> Content-Type: application/json
> Accept: */*
> Content-Length: 69

| {"name": "ziv", "email": "ziv@gmail.com", "password": "newpaassword"}

Response:
200
{
	"message": {
		"_id": "6672eb7ab6512777d43330f1",
		"email": "ziv@gmail.com",
		"name": "ziv",
		"password": "newpaassword"
	}
}

# delete a user
Request:
> DELETE /v1/users/6672eb7ab6512777d43330f1 HTTP/1.1
> Host: localhost:8080
> User-Agent: insomnia/9.2.0
> Accept: */*

Response:
200
{
	"message": "SUCCESS"
}
