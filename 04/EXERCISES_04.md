# Coding Exercises 4 | `Shape` 🔶

## Exercise 1
### Multiple Choice:
Which parameter in the Shape class is used to set the thickness of the shape's outline?

- [ ] `outline_width`
- [ ] `border_thickness`
- [ ] `line_width`
- [ ] `stroke_size`

<details>
<summary>Click here to view the solution</summary>

- [ ] `outline_width`
- [ ] `border_thickness`
- [x] `line_width`
- [ ] `stroke_size`

The `line_width` parameter is used to set the thickness of the shape's outline in the `Shape` class.

</details>

## Exercise 2
### Multiple Choice:
Which class in borb provides a collection of predefined shapes for quick integration?

- [ ] `Shape`
- [ ] `LineArt`
- [ ] `ProgressSquare`
- [ ] `PredefinedShape`

<details>
<summary>Click here to view the solution</summary>

- [ ] `Shape`
- [x] `LineArt`
- [ ] `ProgressSquare`
- [ ] `PredefinedShape`

The `LineArt` class provides a collection of predefined shapes for quick integration in borb.

</details>

## Exercise 3
### Multiple Choice:
What is the correct syntax to create a map of Europe to a PDF document using borb?

- [ ] `MapOfEurope()`
- [ ] `MapOfEurope.add()`
- [ ] `MapOfEurope.create()`
- [ ] `MapOfNorthAmerica.new()`

<details>
<summary>Click here to view the solution</summary>

- [x] `MapOfEurope()`
- [ ] `MapOfEurope.add()`
- [ ] `MapOfEurope.create()`
- [ ] `MapOfNorthAmerica.new()`

The correct syntax to create a map of Europe is `MapOfEurope()`.

</details>

## Exercise 4
### Multiple Choice:
What is the correct syntax to create a custom shape with specific coordinates using the Shape class in borb?

- [ ] `Shape(coordinates=[(0, 0), (50, 50), (100, 0)])`
- [ ] `Shape(points=[(0, 0), (50, 50), (100, 0)])`
- [ ] `Shape(vertices=[(0, 0), (50, 50), (100, 0)])`
- [ ] `Shape(locations=[(0, 0), (50, 50), (100, 0)])`

<details>
<summary>Click here to view the solution</summary>

- [x] `Shape(coordinates=[(0, 0), (50, 50), (100, 0)])`
- [ ] `Shape(points=[(0, 0), (50, 50), (100, 0)])`
- [ ] `Shape(vertices=[(0, 0), (50, 50), (100, 0)])`
- [ ] `Shape(locations=[(0, 0), (50, 50), (100, 0)])`

The correct syntax to create a custom shape with specific coordinates is `Shape(coordinates=[(0, 0), (50, 50), (100, 0)])`.
</details>

## Exercise 5
### Multiple Choice:
Which method would you use to ensure a shape fits within a specific area while maintaining its aspect ratio, and what is the correct syntax?

- [ ] `fit_to_area(width, height)`
- [ ] `resize_to_fit(width, height)`
- [ ] `scale_to_fit(width, height)`
- [ ] `adjust_to_area(width, height)`

<details>
<summary>Click here to view the solution</summary>

- [ ] `fit_to_area(width, height)`
- [ ] `resize_to_fit(width, height)`
- [x] `scale_to_fit(width, height)`
- [ ] `adjust_to_area(width, height)`

The correct method to ensure a shape fits within a specific area while maintaining its aspect ratio is `scale_to_fit(width, height)`.
</details>

## Exercise 6
### Multiple Choice:
If you want to rotate a shape by 90 degrees clockwise, which method and parameter would you use?

- [ ] `rotate(-90)`
- [ ] `rotate(90)`
- [ ] `rotate_clockwise(90)`
- [ ] `rotate_counterclockwise(-90)`

<details>
<summary>Click here to view the solution</summary>

- [ ] `rotate(-90)`
- [x] `rotate(90)`
- [ ] `rotate_clockwise(90)`
- [ ] `rotate_counterclockwise(-90)`

To rotate a shape by 90 degrees clockwise, you would use the `rotate(90)` method.
</details>

## Exercise 7
### Multiple Choice:
You need to add a map of Asia to a PDF document and highlight the country of Japan in red. Which class and method would you use to achieve this?

- [ ] Use `MapOfAsia` with `set_stroke_color(fill_color=X11Color.RED, name="Japan")`
- [ ] Use `MapOfTheWorld` with `highlight_region("Japan", X11Color.RED)`
- [ ] Use `MapOfAsia` with `set_fill_color(fill_color=X11Color.RED, name="Japan")`
- [ ] Use `MapOfAsia` with `set_region_color("Japan", X11Color.RED)`

<details>
<summary>Click here to view the solution</summary>

- [ ] Use `MapOfAsia` with `set_stroke_color(fill_color=X11Color.RED, name="Japan")`
- [ ] Use `MapOfTheWorld` with `highlight_region("Japan", X11Color.RED)`
- [x] Use `MapOfAsia` with `set_fill_color(fill_color=X11Color.RED, name="Japan")`
- [ ] Use `MapOfAsia` with `set_region_color("Japan", X11Color.RED)`

To highlight Japan in red on a map of Asia, you would use `MapOfAsia` with `set_fill_color(fill_color=X11Color.RED, name="Japan")`.
</details>

## Exercise 8
### Multiple Choice:
You need to create a PDF document that includes a custom shape with a thick blue outline and a transparent fill. Which parameters would you adjust in the Shape class?

- [ ] `stroke_color=X11Color.BLUE, line_width=5, fill_color=None`
- [ ] `fill_color=X11Color.BLUE, line_width=5, stroke_color=None`
- [ ] `stroke_color=None, line_width=5, fill_color=X11Color.BLUE`
- [ ] `stroke_color=X11Color.BLUE, line_width=5, fill_color=X11Color.TRANSPARENT`

<details>
<summary>Click here to view the solution</summary>

- [x] `stroke_color=X11Color.BLUE, line_width=5, fill_color=None`
- [ ] `fill_color=X11Color.BLUE, line_width=5, stroke_color=None`
- [ ] `stroke_color=None, line_width=5, fill_color=X11Color.BLUE`
- [ ] `stroke_color=X11Color.BLUE, line_width=5, fill_color=X11Color.TRANSPARENT`

To create a shape with a thick blue outline and a transparent fill, you would use `stroke_color=X11Color.BLUE, line_width=5, fill_color=None`.
</details>

## Exercise 9
### Multiple Choice:
You are designing a PDF document that requires a custom polygonal shape to be mirrored along the vertical axis to create a symmetrical design. Which method would you use, and how would you apply it?

- [ ] Use `rotate(180)` on the shape.
- [ ] Use `mirror_horizontally()` on the shape.
- [ ] Use `mirror_vertically()` on the shape.
- [ ] Use `scale_by_factor(-1)` on the shape.

<details>
<summary>Click here to view the solution</summary>

- [ ] Use `rotate(180)` on the shape.
- [ ] Use `mirror_horizontally()` on the shape.
- [x] Use `mirror_vertically()` on the shape.
- [ ] Use `scale_by_factor(-1)` on the shape.

To create a symmetrical design by mirroring a shape along the vertical axis, you would use the `mirror_vertically` method on the shape.
</details>

## Exercise 10
### Multiple Choice:
How can the `set_fill_color` and `set_stroke_color` methods be used to convey information effectively in a map included in a PDF document?

- [ ] By using random colors for aesthetic purposes
- [ ] By using consistent color schemes to represent different data categories
- [ ] By setting both colors to the same value for uniformity
- [ ] By using only grayscale colors

<details>
<summary>Click here to view the solution</summary>

- [ ] By using random colors for aesthetic purposes
- [x] By using consistent color schemes to represent different data categories
- [ ] By setting both colors to the same value for uniformity
- [ ] By using only grayscale colors

The `set_fill_color` and `set_stroke_color` methods can be used to convey information effectively by using consistent color schemes to represent different data categories, enhancing the map's informational value.
</details>
