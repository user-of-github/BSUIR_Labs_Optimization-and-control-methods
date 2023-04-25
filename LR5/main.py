import pprint
from data import VECTOR_A_EXAMPLE as production_points
from data import VECTOR_B_EXAMPLE as destination_points
from data import VECTOR_C_EXAMPLE as cost_matrix
from get_transportation_plan_by_method_of_potentials import get_transportation_plan_by_method_of_potentials


def main() -> None:
    matrix_transport_problem_solution = get_transportation_plan_by_method_of_potentials(production_points, destination_points, cost_matrix)

    pprint.pprint(matrix_transport_problem_solution)


if __name__ == '__main__':
    main()
