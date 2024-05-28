function cleanSet(set, startString) {
  if (!(set instanceof Set)) {
    throw new TypeError('The first argument must be a Set');
  }
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  const result = Array.from(set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');

  return result;
}

export default cleanSet;
