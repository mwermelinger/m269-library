"""Unit tests for the Deque class."""

from lib.deque import Deque
import pytest

class TestDeque:
    def setup_method(self):
        # Create queues for the tests to use
        self.new = Deque()
        # Test combination of add/remove
        self.empty = Deque()
        self.empty.add_front("hi")
        self.empty.remove_rear()
        # Don't add in ascending or descending order
        self.from_front = Deque()
        self.from_front.add_front(5)
        self.from_front.add_front(2)
        self.from_front.add_front(7)
        self.from_front.add_front(2)
        # Same the other way round
        self.from_rear = Deque()
        self.from_rear.add_rear(2)
        self.from_rear.add_rear(7)
        self.from_rear.add_rear(2)
        self.from_rear.add_rear(5)

    def test_length(self):
        assert (len(self.new) == 0)
        assert (len(self.empty) == 0)
        assert (len(self.from_front) == 4)

    def test_is_empty(self):
        assert (self.new.is_empty())
        assert (self.empty.is_empty())
        assert not (self.from_front.is_empty())

    def test_str(self):
        assert (str(self.new) == str(self.empty))
        assert (str(self.from_front) == str(self.from_rear))

    def test_fifo_order(self):
        assert (self.from_front.remove_rear() == 5)
        assert (self.from_front.remove_rear() == 2)
        assert (self.from_front.remove_rear() == 7)
        assert (self.from_front.remove_rear() == 2)
        # FIFO is opposite order in other deque
        assert (self.from_rear.remove_front() == 2)
        assert (self.from_rear.remove_front() == 7)
        assert (self.from_rear.remove_front() == 2)
        assert (self.from_rear.remove_front() == 5)

    def test_lifo_order(self):
        assert (self.from_front.remove_front() == 2)
        assert (self.from_front.remove_front() == 7)
        assert (self.from_front.remove_front() == 2)
        assert (self.from_front.remove_front() == 5)
        # LIFO is opposite order in other deque
        assert (self.from_rear.remove_rear() == 5)
        assert (self.from_rear.remove_rear() == 2)
        assert (self.from_rear.remove_rear() == 7)
        assert (self.from_rear.remove_rear() == 2)

    def test_access_to_empty(self):
        with pytest.raises(AssertionError):
            self.new.front()
        with pytest.raises(AssertionError):
            self.empty.rear()
        with pytest.raises(AssertionError):
            self.new.remove_rear()
        with pytest.raises(AssertionError):
            self.empty.remove_front()

    def test_membership(self):
        assert not (2 in self.new)
        assert not ("hi" in self.empty)
        assert (2 in self.from_front)
        assert (5 in self.from_front)
        assert (7 in self.from_front)
        assert not (3 in self.from_front)
