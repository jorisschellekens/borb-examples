# Coding Exercises 8 | `PageLayout` 📝

## Exercise 1  
### Multiple Choice:  
Which `PageLayout` automatically creates a new `Page` when space runs out?  

- [ ] `MultiColumnLayout`  
- [ ] `FixedPageLayout`  
- [x] `SingleColumnLayout`  
- [ ] `ManualLayout`  

<details>  
<summary>Click here to view the solution</summary>  

- [ ] `MultiColumnLayout`  
- [ ] `FixedPageLayout`  
- [x] `SingleColumnLayout`  
- [ ] `ManualLayout`  

`SingleColumnLayout` automatically creates a new `Page` in the `Document` when the current page runs out of space.  

</details>  

---

## Exercise 2  
### Multiple Choice:  
Which method allows you to manually move content to the next `Page` in `SingleColumnLayout`?  

- [ ] `next_column()`  
- [ ] `new_page()`  
- [ ] `jump_page()`  
- [x] `next_page()`  

<details>  
<summary>Click here to view the solution</summary>  

- [ ] `next_column()`  
- [ ] `new_page()`  
- [ ] `jump_page()`  
- [x] `next_page()`  

The `next_page()` method forces `SingleColumnLayout` to create a new `Page` and continue placing content there.  

</details>  

---

## Exercise 3  
### True/False:  
In `MultiColumnLayout`, content always moves to a new `Page` before filling all available columns.  

<details>  
<summary>Click here to view the solution</summary>  

False. `MultiColumnLayout` fills all available columns before creating a new `Page`.  

</details>  

---

## Exercise 4  
### Multiple Choice:  
Which method allows you to manually move to the next column in `MultiColumnLayout`?  

- [ ] `next_column()`  
- [ ] `next_page()`  
- [ ] `next_layout()`  
- [ ] `move_right()`  

<details>  
<summary>Click here to view the solution</summary>  

- [x] `next_column()`  
- [ ] `next_page()`  
- [ ] `next_layout()`  
- [ ] `move_right()`  

The `next_column()` method forces `MultiColumnLayout` to start placing content in the next column before filling the current one.  

</details>  

---

## Exercise 5  
### Multiple Choice:  
Which statement is true about manually placing a `LayoutElement` using `paint()`?  

- [ ] It automatically integrates with `SingleColumnLayout`.  
- [ ] It allows precise placement of elements on the page.  
- [ ] It requires `MultiColumnLayout` to function.  
- [ ] It only works for `Paragraph` elements.  

<details>  
<summary>Click here to view the solution</summary>  

- [ ] It automatically integrates with `SingleColumnLayout`.  
- [x] It allows precise placement of elements on the page.  
- [ ] It requires `MultiColumnLayout` to function.  
- [ ] It only works for `Paragraph` elements.  

Using `paint()`, you can manually place `LayoutElement` objects with exact positioning, independent of `PageLayout`.  

</details>  
