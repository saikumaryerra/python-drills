def html_dict_search(html_dict, selector):
    """
    Implement `id` and `class` selectors
    """
    lst = []
    x = html_dict["attrs"]
    new_selector = selector[1:]
    if selector[:1] == ".":
        if "class" in x:
            if x["class"] == new_selector:
                lst.append(html_dict)
    elif selector[:1] == "#":
        if "id" in x:
            if x["id"] == new_selector:
                lst.append(html_dict)
    else:
        print("not a selector")
    for i in html_dict["children"]:
                    lst.extend(html_dict_search(i, selector))
    return lst


# a = {"name": "main-head",
#      "attrs": {
#      "id":"saii"
#      },
#      "children": [
#          {"name": "head", "attrs": {"id": "saii"}, "children": [{"name": "main_test", "attrs": {"id": "saii"}, "children": []}]},
#          {"name": "test1", "attrs": {}, "children": []}
#      ]
#      }
# x = html_dict_search(a, '#saii')
# print(x)
