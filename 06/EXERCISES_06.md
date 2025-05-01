# Coding Exercises 6 | `List` & `Table` 📋

## Exercise 1
### Multiple Choice:
When you want to create a bullet-pointed list without any specific ordering, which `borb` class should you use?

- [ ] `OrderedList`
- [ ] `UnorderedList`
- [ ] `BulletList`
- [ ] `ABCOrderedList`

<details>
<summary>Click here to view the solution</summary>

- [ ] `OrderedList`
- [x] `UnorderedList`
- [ ] `BulletList`
- [ ] `ABCOrderedList`

The `UnorderedList` class is used to create bullet-pointed lists without specific ordering.

</details>

## Exercise 2
### Multiple Choice:
Which method is used to add items to a list in `borb`?

- [ ] `add_item()`
- [ ] `append_layout_element()`
- [ ] `insert_element()`
- [ ] `add_to_list()`

<details>
<summary>Click here to view the solution</summary>

- [ ] `add_item()`
- [x] `append_layout_element()`
- [ ] `insert_element()`
- [ ] `add_to_list()`

The `append_layout_element()` method is used to add items to a list in `borb`.
</details>

## Exercise 3
### Multiple Choice:
In `borb`, how do you make a table cell span multiple columns?

- [ ] Set the `col_span` parameter when adding the cell
- [ ] Use the `span_columns` method on the cell
- [ ] Set the `column_span` parameter in the `TableCell`
- [ ] Merge cells after creating the table

<details>
<summary>Click here to view the solution</summary>

- [ ] Set the `col_span` parameter when adding the cell
- [ ] Use the `span_columns` method on the cell
- [x] Set the `column_span` parameter in the `TableCell`
- [ ] Merge cells after creating the table

To make a table cell span multiple columns, you set the `column_span` parameter in the `TableCell`.
</details>

## Exercise 4
### Multiple Choice:
How can you nest one `List` inside another `List` in `borb`?

- [ ] By using the `nest()` method
- [ ] By adding the inner list as an item using `append_layout_element()`
- [ ] By setting the `parent_list` property
- [ ] By calling `add_nested_list()`

<details>
<summary>Click here to view the solution</summary>

- [ ] By using the `nest()` method
- [x] By adding the inner list as an item using `append_layout_element()`
- [ ] By setting the `parent_list` property
- [ ] By calling `add_nested_list()`

You nest a `List` inside another by adding the inner list as an item using `append_layout_element()`.
</details>

## Exercise 5
### Multiple Choice:
Which method would you use to remove all borders from a table EXCEPT the outer edges?

- [ ] `remove_borders()`
- [ ] `no_borders()`
- [ ] `no_external_borders()`
- [ ] `no_internal_borders()`

<details>
<summary>Click here to view the solution</summary>

- [ ] `remove_borders()`
- [ ] `no_borders()`
- [ ] `no_external_borders()`
- [x] `no_internal_borders()`

`no_internal_borders()` removes only the internal borders while keeping the external borders intact.
</details>

## Exercise 6
### True/False:
In a `TableCell`, setting `row_span=2` and `column_span=3` will create a cell that occupies 5 total grid spaces in the table.

<details>
<summary>Click here to view the solution</summary>

False. When a `TableCell` has both `row_span=2` and `column_span=3`, it will occupy a 2x3 grid of cells, resulting in 6 total grid spaces in the table.
</details>
