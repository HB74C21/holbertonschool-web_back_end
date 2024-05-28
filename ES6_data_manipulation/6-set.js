function setFromArray(arr) {
  if (!Array.isArray(arr)) {
    throw new TypeError('Input must be an array');
  }
  return new Set(arr);
}

export default setFromArray;
