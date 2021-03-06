import pytest
from linked_list.linked_list import Node, LinkedList, DoublyNode, DoublyLinkedList


#============================================
#===========    Required Tests    ===========
#============================================


def test_empty_list_instatiation():
    assert LinkedList().head is None


def test_inserting_into_linked_list(my_linked_list):
    my_linked_list.Insert(Node("Barham"))
    assert str(my_linked_list) == "Barham -> Mustafa -> Zaid -> Ammar -> NULL"


def test_head_pointer_towards_first_node(my_linked_list):
    assert my_linked_list.head.value == Node("Mustafa").value


def test_inserting_multiple_nodes(my_linked_list):
    [my_linked_list.Insert(Node(i)) for i in ["Barham", "Imad", "Husain"]]
    assert str(my_linked_list) == "Husain -> Imad -> Barham -> Mustafa -> Zaid -> Ammar -> NULL"


def test_serching_for_existed_node(my_linked_list):
    assert my_linked_list.Includes("Zaid") == True


def test_serching_for_not_existed_node(my_linked_list):
    assert my_linked_list.Includes("Maher") == False


def test_returning_all_values_in_linked_list(my_linked_list):
    assert str(my_linked_list) == "Mustafa -> Zaid -> Ammar -> NULL"


#==============================================
#===========    Challenge 06 tests   ==========
#==============================================


def test_appending_to_linked_list(my_linked_list):
    my_linked_list.Append(Node("Barham"))
    assert str(my_linked_list) == "Mustafa -> Zaid -> Ammar -> Barham -> NULL"


def test_providing_not_node_instance_for_append_method(my_linked_list):
    my_linked_list.Append("Barham")
    assert str(my_linked_list) == "Mustafa -> Zaid -> Ammar -> Barham -> NULL"


def test_inserting_a_node_before_a_specific_other_node(my_linked_list):
    my_linked_list.InsertBefore("Zaid", "Barham")
    assert str(my_linked_list) == "Mustafa -> Barham -> Zaid -> Ammar -> NULL"


def test_inserting_a_node_before_the_head(my_linked_list):
    my_linked_list.InsertBefore("Mustafa", "Barham")
    assert str(my_linked_list) == "Barham -> Mustafa -> Zaid -> Ammar -> NULL"


def test_inserting_a_node_after_the_last_node(my_linked_list):
    my_linked_list.InsertAfter("Ammar", "Barham")
    assert str(my_linked_list) == "Mustafa -> Zaid -> Ammar -> Barham -> NULL"


def test_inserting_a_node_after_a_specific_other_node(my_linked_list):
    my_linked_list.InsertAfter("Zaid", "Barham")
    assert str(my_linked_list) == "Mustafa -> Zaid -> Barham -> Ammar -> NULL"


def test_deleting_the_head(my_linked_list):
    my_linked_list.Delete("Mustafa")
    assert str(my_linked_list) == "Zaid -> Ammar -> NULL"


def test_deleting_a_middle_node(my_linked_list):
    my_linked_list.Delete("Zaid")
    assert str(my_linked_list) == "Mustafa -> Ammar -> NULL"


def test_deleting_the_last_node(my_linked_list):
    my_linked_list.Delete("Ammar")
    assert str(my_linked_list) == "Mustafa -> Zaid -> NULL"


#==============================================
#===========    Challenge 07 tests   ==========
#==============================================


def test_Length_linked_list(my_long_linked_list):
    assert my_long_linked_list.Length() == 6


def test_kthFromEnd_at_0(my_long_linked_list):
    assert my_long_linked_list.kthFromEnd(0) == "Husain"


def test_kthFromEnd_in_the_middle(my_long_linked_list):
    assert my_long_linked_list.kthFromEnd(2) == "Barham"


def test_kthFromEnd_at_the_begining(my_long_linked_list):
    assert my_long_linked_list.kthFromEnd(5) == "Mustafa"


def test_kthFromEnd_for_list_of_size_1():
    ll = LinkedList()
    ll.Append("Mustafa") 
    assert ll.kthFromEnd(0) == "Mustafa"


def test_kthFromEnd_where_k_is_greater_than_length(my_long_linked_list):
    with pytest.raises(Exception):
        my_long_linked_list.kthFromEnd(10)

#==============================================
#===========    Challenge 08 tests   ==========
#==============================================

def test_ziplists_for_identical_length_lists(my_linked_list, numeric_list):
    actual = str(LinkedList.zipLists(my_linked_list, numeric_list))
    expected = "Mustafa -> 0 -> Zaid -> 1 -> Ammar -> 2 -> NULL"
    assert actual == expected


def test_ziplists_for_list1_is_longer(my_linked_list, long_numeric_list):
    actual = str(LinkedList.zipLists(long_numeric_list, my_linked_list))  
    expected = "0 -> Mustafa -> 1 -> Zaid -> 2 -> Ammar -> 3 -> 4 -> 5 -> NULL"
    assert actual == expected


def test_ziplists_for_list2_is_longer(my_linked_list, long_numeric_list):
    actual = str(LinkedList.zipLists(my_linked_list, long_numeric_list)) 
    expected = "Mustafa -> 0 -> Zaid -> 1 -> Ammar -> 2 -> 3 -> 4 -> 5 -> NULL"
    assert actual == expected


def test_ziplists_for_one_list_is_empty(my_linked_list):
    assert str(LinkedList.zipLists(my_linked_list, LinkedList())) == "Mustafa -> Zaid -> Ammar -> NULL"
    assert str(LinkedList.zipLists(LinkedList(), my_linked_list)) == "Mustafa -> Zaid -> Ammar -> NULL"


def test_ziplists_for_providing_not_list():
    with pytest.raises(Exception):
        LinkedList.zipLists("hello", 5)



#==============================================
#===========    Additional Tests    ===========
#==============================================


def test_providing_not_node_instance_for_insert_method(my_linked_list):
    my_linked_list.Insert("Barham")
    assert str(my_linked_list) == "Barham -> Mustafa -> Zaid -> Ammar -> NULL"


def test_providing_a_node_instance_for_includes_method(my_linked_list):
    assert my_linked_list.Includes(Node("Zaid")) == True


def test_replacing_the_head_with_another_node(my_linked_list):
    my_linked_list.Replace("Mustafa", "Barham")
    assert str(my_linked_list) == "Barham -> Zaid -> Ammar -> NULL"


def test_replacing_a_node_in_the_middle_with_another_node(my_linked_list):
    my_linked_list.Replace("Zaid", "Barham")
    assert str(my_linked_list) == "Mustafa -> Barham -> Ammar -> NULL"


def test_replacing_the_last_node_with_another_node(my_linked_list):
    my_linked_list.Replace("Ammar", "Barham")
    assert str(my_linked_list) == "Mustafa -> Zaid -> Barham -> NULL"


def test_slicing_the_linked_list(my_long_linked_list):
    new_list = my_long_linked_list.Slice(From="Zaid", To="Barham")
    assert str(new_list) == "Zaid -> Ammar -> Barham -> NULL"


def test_slicing_the_linked_list_from_the_head(my_long_linked_list):
    new_list = my_long_linked_list.Slice(From="Mustafa", To="Barham")
    assert str(new_list) == "Mustafa -> Zaid -> Ammar -> Barham -> NULL"


def test_slicing_the_linked_list_to_the_end(my_long_linked_list):
    new_list = my_long_linked_list.Slice(From="Barham", To="Husain")
    assert str(new_list) == "Barham -> Imad -> Husain -> NULL"


def test_reversing_the_linked_list(my_linked_list):
    new_list = my_linked_list.Reverse()
    assert str(new_list) == "Ammar -> Zaid -> Mustafa -> NULL"


#==================================================
#===========    Streach goal (Doubly)   ===========
#==================================================


def test_doubly_linked_list_ToString_meyhod(my_doubly_linked_list):
    my_doubly_linked_list.ToString()
    assert str(my_doubly_linked_list) == "NULL <- Mustafa <-> Zaid <-> Ammar -> NULL"


def test_doubly_linked_list_Insert_meyhod(my_doubly_linked_list):
    my_doubly_linked_list.Insert("Barham")
    assert str(my_doubly_linked_list) == "NULL <- Barham <-> Mustafa <-> Zaid <-> Ammar -> NULL"


def test_doubly_linked_list_Append_meyhod(my_doubly_linked_list):
    my_doubly_linked_list.Append("Barham")
    assert str(my_doubly_linked_list) == "NULL <- Mustafa <-> Zaid <-> Ammar <-> Barham -> NULL"


def test_doubly_linked_list_Includes_meyhod(my_doubly_linked_list):
    assert my_doubly_linked_list.Includes("Zaid") == True


def test_doubly_linked_list_Includes_meyhod(my_doubly_linked_list):
    assert my_doubly_linked_list.Includes("Husain") == False
    

def test_doubly_linked_list_Replace_meyhod(my_doubly_linked_list):
    my_doubly_linked_list.Replace("Zaid", "Barham")
    assert str(my_doubly_linked_list) == "NULL <- Mustafa <-> Barham <-> Ammar -> NULL"


def test_doubly_linked_list_Delete_meyhod(my_doubly_linked_list):
    my_doubly_linked_list.Delete("Zaid")
    assert str(my_doubly_linked_list) == "NULL <- Mustafa <-> Ammar -> NULL"


def test_doubly_linked_list_Slice_meyhod(my_long_doubly_linked_list):
    new_list = my_long_doubly_linked_list.Slice(From="Zaid", To="Barham")
    assert str(new_list) == "NULL <- Zaid <-> Ammar <-> Barham -> NULL"


def test_doubly_linked_list_Reverse_meyhod(my_doubly_linked_list):
    new_list = my_doubly_linked_list.Reverse()
    assert str(new_list) == "NULL <- Ammar <-> Zaid <-> Mustafa -> NULL"


#======================================
#===========    Fixtures    ===========
#======================================


@pytest.fixture
def my_linked_list():
    ll = LinkedList()
    [ll.Append(Node(i)) for i in ["Mustafa", "Zaid", "Ammar"]]
    return ll


@pytest.fixture
def my_long_linked_list():    
    ll = LinkedList()
    [ll.Append(Node(i)) for i in ["Mustafa", "Zaid", "Ammar", "Barham", "Imad", "Husain"]]
    return ll


@pytest.fixture
def my_doubly_linked_list():    
    dll = DoublyLinkedList()
    [dll.Append(DoublyNode(i)) for i in ["Mustafa", "Zaid", "Ammar"]]
    return dll


@pytest.fixture
def my_long_doubly_linked_list():    
    dll = DoublyLinkedList()
    [dll.Append(DoublyNode(i)) for i in ["Mustafa", "Zaid", "Ammar", "Barham", "Imad", "Husain"]]
    return dll


@pytest.fixture
def numeric_list():
    ll = LinkedList()
    [ll.Append(i) for i in range(3)]
    return ll


@pytest.fixture
def long_numeric_list():
    ll = LinkedList()
    [ll.Append(i) for i in range(6)]
    return ll