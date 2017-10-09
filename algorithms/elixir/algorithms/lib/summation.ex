defmodule Summation do
  @moduledoc """
  Implements various algorithms for summation.
  """

  @doc """
  Computes the sum of a list using down-by-one recursion.
  ## Examples
      iex> Summation.sum_dbo([1, 3, 2, 4, 3, 5])
      18
  """
  def sum_dbo(list) do
    case list do
      [] -> 0
      [head | tail] -> head + sum_dbo(tail)
    end
  end

  @doc """
  Computes the sum of a list using division-in-halves recursion.
  ## Examples
      iex> Summation.sum_halves([1, 4, 2, 5, 3, 6])
      21
  """
  def sum_halves(list) do
    case list do
      [] -> 0
      [x] -> x
      {left_half, right_half} -> sum_halves(left_half) + sum_halves(right_half)
      _ -> sum_halves(Enum.split(list, div(length(list), 2)))
    end
  end
end
