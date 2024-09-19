const fs = require('fs').promises;

function countStudents(path) {
    return fs.readFile(path, 'utf8')
        .then((data) => {
            // Diviser les lignes du fichier CSV
            const lines = data.split('\n').filter((line) => line.trim().length > 0);

            // Ignorer la première ligne (en-tête)
            const students = lines.slice(1);

            // Si le fichier ne contient aucun étudiant
            if (students.length === 0) {
                console.log('Number of students: 0');
                return;
            }

            // Compter le nombre total d'étudiants
            console.log(`Number of students: ${students.length}`);

            // Créer des objets pour stocker les étudiants par domaine
            const fields = {};

            students.forEach((student) => {
                const [firstname, , , field] = student.split(',');

                if (field) {
                    if (!fields[field]) {
                        fields[field] = [];
                    }
                    fields[field].push(firstname);
                }
            });

            // Afficher le nombre d'étudiants et leurs prénoms par domaine
            for (const field in fields) {
                if (fields.hasOwnProperty(field)) {
                    const studentsList = fields[field];
                    console.log(
                        `Number of students in ${field}: ${studentsList.length}. List: ${studentsList.join(', ')}`
                    );
                }
            }
        })
        .catch(() => {
            throw new Error('Cannot load the database');
        });
}

module.exports = countStudents;