#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <stdlib.h>


int main(int argc, char **argv)
{
	int fd;
	int gain, offset_dac, gain_adc, offset_adc;
	uint32_t count;
	void *cfg;
	char *name= "/dev/mem";
	const int  freq = 1249988750;
	if (argc == 5) {
		gain = atof(argv[1]);
		offset_dac = atof(argv[2]);
		gain_adc = atof(argv[3]);
		offset_adc = atof(argv[4]);
	}
	else {
		gain = 2048;
		offset_dac = 82;
		gain_adc = 4252;
		offset_adc = 228;
	}
	if ((fd = open(name, O_RDWR)) < 0) {
		perror("open");
		return 1;
	}
	cfg = mmap(NULL, sysconf(_SC_PAGESIZE), PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0x40000000);
	*((uint32_t *)(cfg + 0)) = gain;
	*((uint32_t *)(cfg + 4)) = offset_dac;
	*((uint32_t *)(cfg + 8)) = gain_adc;
	*((uint32_t *)(cfg + 12)) = offset_adc;
}

