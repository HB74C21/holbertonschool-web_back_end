function getListStudentIds(arr) {
  return Array.isArray(arr) ? arr.map((student) => student.id) : [];
}

export default getListStudentIds;
