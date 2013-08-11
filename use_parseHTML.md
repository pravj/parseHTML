=======
> <b>source = 'sample HTML to play with'</b><br>
> <b>parse &nbsp; = parseHTML(source)</b><br>
  
=======

**Method**
==========
> <b>parse.count(<i>tag</i>)</b>

  &nbsp; &nbsp;  <code>returns <b>number</b> of total tags(<b>tag</b>) in the supplied content</code>
  
> <b>parse.isAttr(<i>toCheck</i>, <i>attr</i>)</b>

  &nbsp; &nbsp;  <code>return <code>__True__</code></code>, if <code>**attr**</code>, found in <code>**toCheck**</code><br>
  &nbsp; &nbsp;  <code>return :<code>__False__</code></code>, if <code>**attr**</code> not found
  
> <b>parse.isValue(<i>toCheck</i>, <i>value</i>)</b>

  &nbsp; &nbsp;  <code>return <code>__True__</code></code>, if <code>**value**</code>, found in <code>**toCheck**</code><br>
  &nbsp; &nbsp;  <code>return :<code>__False__</code></code>, if <code>**value**</code> not found
  
> <b>parse.tag_Data(<i>tag</i>)</b>

  &nbsp; &nbsp; <code>return a <b>List</b> of data inside all tags(<b>tag</b>)</code>
  
> <b>parse.Attr_Value(<i>toCheck</i>,<i>attr</i>)</b>

  &nbsp; &nbsp; <code>return <b>Attribute</b>(<i>attr</i>)'s Value in <b>toCheck</b></code>
  
> <b>parse.insideValue(<i>tag</i>)</b>

  &nbsp; &nbsp; <code>return <b>string</b> containing <b>Attribute(<i>attr</i>)</b>'s {<b>key, value</b>} for all tags(<b>tag</b>)</code><br>
  
