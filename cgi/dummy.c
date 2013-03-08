#include <stdlib.h>
#include <string.h>


char* hello_world(int times) {
	static const char* str = "Hello World!";
	size_t len = sizeof(char) * strlen(str) + sizeof(char);
	//	printf("%d\n", len);
	size_t size = (len - 1) * times + (times - 1) * sizeof(char) + sizeof(char);
	char* ret = malloc(size);
	size_t idx = 0;

	//	printf("size: %d\n", size);

	// init to zeroes
	memset(ret, 0, size);
 
	// Oh, the huge manatee!
_do:
	
	strncpy(ret + idx, str, len - sizeof(char));
	idx += len - sizeof(char);
	--times;

	if(times == 0)
			return ret;

	ret[idx] = ' ';
	idx += sizeof(char);

	// eh eh
	goto _do;	

}

//#define EXEC
#ifdef EXEC

void main(void) {
	printf("%s, %d\n", hello_world(6), strlen(hello_world(6)));
	printf("%s, %d\n", hello_world(1), strlen(hello_world(1)));
}

#endif
