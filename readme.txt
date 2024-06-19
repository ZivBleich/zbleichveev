docker build -t myimage . ; docker run -it -p 8080:8080 myimage

####################### Examples:
#### create a user
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
		"password": "********"
	}
}
200

#### list users
Request:
> GET /v1/users HTTP/1.1
> Host: localhost:8080
> Accept: */*

Response:
200
{
	"message": [
		{
			"_id": "6672ec0cb6512777d43330f2",
			"email": "ziv@gmail.com",
			"name": "ziv",
			"password": "********"
		}
	]
}

#### login
> POST /v1/login HTTP/1.1
> Host: 127.0.0.1:8080
> Content-Type: application/json
> Accept: */*
> Content-Length: 43

| {"name": "ziv", "password": "12345678"}

Response:
200
{
	"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxODgxMTI2OSwianRpIjoiM2U0NTJiYzItYTg3NC00YjA1LWFjMTMtNmY4MzZmNjlhZTcyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY2NzJmOTUwNWQwOGNiZGEzMGQyZmE3MiIsIm5iZiI6MTcxODgxMTI2OSwiY3NyZiI6IjcxM2YyNWQ4LTA2NTEtNDNjMy1hYTJhLTI2ZWQ4YmU0NzYwOCIsImV4cCI6MTcxODgxMjE2OX0.A5w2-8JpI-0H39QeeIh0eycw-lh-w6EOSOyoaqlROWU"
}



#### update a user
Request:
> PATCH /v1/users/6672ec0cb6512777d43330f2 HTTP/1.1
> Host: 127.0.0.1:8080
> Content-Type: application/json
> Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxODgxMTAyOCwianRpIjoiZTNiYmI5OTMtNzk2Zi00NWNiLTgzMmUtZDU4OWI5YjlkMWViIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY2NzJmOTUwNWQwOGNiZGEzMGQyZmE3MiIsIm5iZiI6MTcxODgxMTAyOCwiY3NyZiI6IjhkODViM2JiLTc2MTMtNGRkOS1hNzIwLTNjMTFjNWZhYzlkMiIsImV4cCI6MTcxODgxMTkyOH0.FV_5QtpGUmfY98tOVMaprNF9yYALzXzpnvY-dHs4v1k
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
		"password": "********"
	}
}

#### delete a user
> DELETE /v1/users/6672f9505d08cbda30d2fa72 HTTP/1.1
> Host: localhost:8080
> Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxODgxMTI2OSwianRpIjoiM2U0NTJiYzItYTg3NC00YjA1LWFjMTMtNmY4MzZmNjlhZTcyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY2NzJmOTUwNWQwOGNiZGEzMGQyZmE3MiIsIm5iZiI6MTcxODgxMTI2OSwiY3NyZiI6IjcxM2YyNWQ4LTA2NTEtNDNjMy1hYTJhLTI2ZWQ4YmU0NzYwOCIsImV4cCI6MTcxODgxMjE2OX0.A5w2-8JpI-0H39QeeIh0eycw-lh-w6EOSOyoaqlROWU
> Accept: */*

Response:
200
{
	"message": "SUCCESS"
}
