function hasValuesFromArray(set, arr) {
  if (!(set instanceof Set)) {
    throw new TypeError('First argument must be a Set');
  }

  if (!Array.isArray(arr)) {
    throw new TypeError('Second argument must be an Array');
  }

  return arr.every((value) => set.has(value));
}

export default hasValuesFromArray;
