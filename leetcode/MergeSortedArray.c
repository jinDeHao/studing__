#include <stdio.h>
#include <stdlib.h>

void add(int *array, int index, int size, int new_value)
{
	int temp = new_value, j = index;
	if (index >= size)
		return;
	while (j < size)
	{
		temp = array[j];
		array[j] = new_value;
		new_value = temp;
		j++;
	}
}

void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n)
{
	int i = 0, j = 0;
	while (i < m)
	{
		if (j < n && nums1[i] > nums2[j])
		{
			add(nums1, i, nums1Size, nums2[j]);
			m++;
			j++;
		}
		// else
		// {
		// 	i++;
		// }
		i++;
	}
	while (j < n)
	{
		nums1[i++] = nums2[j++];
	}
}

int main()
{
	int nums1[] = {4, 0, 0, 0, 0, 0};
	int nums2[] = {1, 2, 3, 5, 6};

	merge(nums1, 6, 1, nums2, 5, 5);

	for (int i = 0; i < 6; i++)
		printf("%d\n", nums1[i]);

	return (0);
}
