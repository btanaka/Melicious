%include header_template title='All Bookmarks'
%import re



<div class="addstuff">
<button>Add a new bookmark</button>
<div style="display: none">
%include add_template
</div>
<script>
    $("button").click(function () {
    $("div").show("slow");
    });
</script>
</div>




<div class="tagsblock">
Tags:
%for tagrow in tagrows:
  %for s in tagrow:
    <a href="">{{s}}</a> |
  %end
%end
</div>



<div class="tableblock">
<table  cellpadding="0px" cellspacing="0px">
%for row in rows:
  %for r in row:
    %if re.search("^http", r):
      <tr>
      <td><a href="{{r}}">{{r}}</a> </td>
      %#remove all protocol and leading colon slash slash
      %p = re.compile('^.+://')
      %noslash = p.sub( '', r)
      %#change slashes to triple colon so the routing doesn't get confused
      %p = re.compile('/')
      %noslash = p.sub( ':::', noslash)
      %cururl = noslash
    %else: 
      <td>{{r}}</td>
      <td><a href="/delete/{{cururl}}">X</a></td>
      </tr>
    %end
  %end
%end
</table>
<div>


%include footer_template
