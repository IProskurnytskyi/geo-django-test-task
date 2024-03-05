# geo-django-test-task

### You can retrieve an image from api/retrieve-image/ using this format:

```shell
{
  "polygon": {
    "type": "Polygon",
    "coordinates": [
      [
        [0, 0],
        [0, 10],
        [10, 10],
        [10, 0],
        [0, 0]
      ]
    ]
  }
}
```

### You can create a field using this format:

```shell
{
  "name": "YourField",
  "boundary": {
    "type": "Polygon",
    "coordinates": [
      [
        [0, 0],
        [0, 10],
        [10, 10],
        [10, 0],
        [0, 0]
      ]
    ]
  }
}
```