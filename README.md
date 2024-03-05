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

### You can create fields using this format:

```shell
{
  "name": "Field N1",
  "boundary": {
    "type": "Polygon",
    "coordinates": [
      [
        [5, 0],
        [5, 15],
        [15, 15],
        [15, 0],
        [5, 0]
      ]
    ]
  }
}
```

```shell
{
  "name": "Field N2",
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

### You can retrieve fields that intersect with the polygon using data below:

```shell
{
  "polygon": {
    "type": "Polygon",
    "coordinates": [
      [
        [2, 2],
        [2, 8],
        [8, 8],
        [8, 2],
        [2, 2]
      ]
    ]
  }
}
```

### Or you try polygon below that will not intersect with any of the fields above:

```shell
{
  "polygon": {
    "type": "Polygon",
    "coordinates": [
      [
        [20, 20],
        [20, 30],
        [30, 30],
        [30, 20],
        [20, 20]
      ]
    ]
  }
}
```