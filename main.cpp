#include <iostream>
#include <time.h>
#include <fstream>
#include <map>
#include <vector>

int main(void) {
	std::ofstream out("values.txt");
	std::map<int, int> map{};
	int ten = 1;
	for (int i = 0; i <= 7; i++) {
		map.clear();
		for (int l=0; l < ten; l++) map[l] = l;
		out << ten << ' ' << clock() << ' ' << ((sizeof(int) + sizeof(int)) * map.size()) + sizeof(map) << "\n";
		ten *= 10;
	}

	out.close();
	return 0;
}