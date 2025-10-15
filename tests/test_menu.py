import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.menu import flatten_menu

# ---- Normal (4) ----
def test_single_item():
    assert flatten_menu({"type":"item","name":"Espresso"}) == ["Espresso"]

def test_simple_category():
    node = {"type":"category","name":"Menu","children":[
        {"type":"item","name":"Americano"},
        {"type":"item","name":"Latte"},
    ]}
    assert flatten_menu(node) == ["Americano","Latte"]

def test_nested_category():
    node = {"type":"category","name":"Menu","children":[
        {"type":"item","name":"Americano"},
        {"type":"category","name":"Sandwiches","children":[
            {"type":"item","name":"BLT"},
            {"type":"item","name":"Club"},
        ]},
        {"type":"item","name":"Mocha"},
    ]}
    assert flatten_menu(node) == ["Americano","BLT","Club","Mocha"]

def test_deeper_nesting():
    node = {"type":"category","name":"Menu","children":[
        {"type":"category","name":"A","children":[
            {"type":"item","name":"x"},
            {"type":"category","name":"B","children":[{"type":"item","name":"y"}]}
        ]},
        {"type":"item","name":"z"}
    ]}
    assert flatten_menu(node) == ["x","y","z"]

# ---- Edge (3) ----
def test_empty_category():
    assert flatten_menu({"type":"category","name":"Empty","children":[]}) == []

def test_missing_type():
    assert flatten_menu({"name":"??"}) == []

def test_item_without_name():
    assert flatten_menu({"type":"item"}) == []

# ---- Complex (3) ----
def test_wide_menu():
    node = {"type":"category","name":"M","children":[
        {"type":"item","name":str(i)} for i in range(50)
    ]}
    assert flatten_menu(node) == [str(i) for i in range(50)]

def test_many_nested_levels():
    node = {"type":"item","name":"end"}
    for i in range(30):
        node = {"type":"category","name":f"C{i}","children":[node]}
    assert flatten_menu(node) == ["end"]

def test_mix_weird_nodes_ignored():
    node = {"type":"category","name":"M","children":[
        {"type":"weird","name":"?"},
        {"type":"item","name":"OK"},
        {"no":"type"},
        {"type":"category","name":"Sub","children":[{"type":"item","name":"Fine"}]}
    ]}
    assert flatten_menu(node) == ["OK","Fine"]
