#include "checksum.hpp"

/* [NOTE]:
 * This checksum function was found on:
 * https://stackoverflow.com/questions/3463976/c-file-checksum
 */
unsigned char checksum(FILE *fp) {
     unsigned char sum = 0;
     while (!feof(fp) && !ferror(fp)) {
          sum ^= fgetc(fp);
     }
     return sum;
}