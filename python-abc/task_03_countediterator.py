#!/usr/bin/env python3
"""
CountedIterator - Keeping Track of Iteration

Wraps any iterable's iterator, counts how many items have been produced.
Usage matches Python's iterator protocol (supports next() and for-loops).
"""

from __future__ import annotations
from typing import Iterable, Iterator, TypeVar, Generic

T = TypeVar("T")


class CountedIterator(Generic[T], Iterator[T]):
    """
    An iterator wrapper that counts how many items were iterated.
    """

    def __init__(self, iterable: Iterable[T]) -> None:
        # Underlying iterator we delegate to
        self._it: Iterator[T] = iter(iterable)
        # Number of successfully fetched items
        self._count: int = 0

    def __iter__(self) -> "CountedIterator[T]":
        return self

    def __next__(self) -> T:
        # Delegate to the underlying iterator; only increment if successful
        item = next(self._it)  # may raise StopIteration (desired behavior)
        self._count += 1
        return item

    def get_count(self) -> int:
        """Return the number of items that have been yielded so far."""
        return self._count
