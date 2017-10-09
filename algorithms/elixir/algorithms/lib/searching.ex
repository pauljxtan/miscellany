defmodule Searching do
  @moduledoc """
  Implements various algorithms for searching lists.
  """

  @doc """
  Performs an unstable binary search on a sorted list.
  Returns the index if found, otherwise returns :not_found.
  ## Examples
  iex> Searching.binary_search([1, 2, 4, 7, 11], 7)
  3  
  iex> Searching.binary_search([1, 2, 4, 7, 11], 9)
  :not_found
  """
  def binary_search(list, value) do
    case list do
      [] -> :not_found
      [value] -> value
      _ -> binary_search(list ,value, 0, length(list) - 1)
    end
  end
  def binary_search(list, value, left_index, right_index) do
    mid_index = div(left_index + right_index, 2)
    mid_value = Enum.at(list, mid_index)
    cond do
      right_index < left_index -> :not_found
      value == mid_value -> mid_index
      value < mid_value -> binary_search(list, value, left_index, right_index - 1)
      value > mid_value -> binary_search(list, value, mid_index + 1, right_index)
    end
  end
end
