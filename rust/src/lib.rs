#[warn(non_snake_case)]
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use simple_matrix::Matrix;
use std::cmp;
use std::convert::TryInto;

#[pymodule]
fn needleman_wunsch_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(get_score))?;

    Ok(())
}

#[pyfunction]
fn get_score(_seq1: String, _seq2: String) -> PyResult<f64> {
    let mut sequences: Vec<String> = change_sequences(_seq1, _seq2);
    
    let _seq11: String = sequences.pop().unwrap();
    let _seq21: String = sequences.pop().unwrap();

    let seq1_vec: Vec<char> = _seq11.chars().collect();
    let seq2_vec: Vec<char> = _seq21.chars().collect();

    let _mat: Matrix<isize> = initialize_matrix(_seq11, _seq21, 1, -1, -1);

    let result: f64 = score();

    Ok(result)
}



//FUNCIONES PRINCIPALES

fn initialize_matrix(
    _seq1: Vec<char>,
    _seq2: Vec<char>,
    _mach: isize,
    _gap: isize,
    _mismatch: isize,
) -> Matrix<isize> {
    //Creamos la matriz
    let row_size = _seq1.len() + 1;
    let col_size = _seq2.len() + 1;
    let mut _mat: Matrix<isize> = Matrix::new(row_size, col_size);

    //Inicializamos la matriz
    let mut pos = 0;
    for i in 0..row_size {
        let score = pos * _gap;
        _mat.set(i, 0, score);
        pos += 1;
    }

    pos = 0;
    for j in 0..col_size {
        let score = pos * _gap;
        _mat.set(0, j, score.try_into().unwrap());
        pos += 1;
    }
    //Creamos la matriz con los pesos

    for i in 1..row_size {
        for j in 1..col_size {
            //Opción 1 - Miramos la puntuación con la diagonal
            let _nuc1 = _seq1[i - 1];
            let _nuc2 = _seq2[j - 1];
            let opcion1;

            if _nuc1 == _nuc2 {
                opcion1 = _mat.get(i - 1, j - 1).unwrap() + _mach;
            } else {
                opcion1 = _mat.get(i - 1, j - 1).unwrap() + _mismatch;
            }

            //Opción 2 - Miramos la puntuación con la de arriba
            let opcion2 = _mat.get(i - 1, j).unwrap() + _mismatch;

            //Opción 3 - Miramos la puntuación con la izquierda
            let opcion3 = _mat.get(i, j - 1).unwrap() + _mismatch;

            //Escogemos y guardamos el valor máximo de las tres opciones
            let mut max = cmp::max(opcion1, opcion2);
            max = cmp::max(max, opcion3);
            _mat.set(i, j, max);
        }
    }

    _mat
}

fn change_sequences(mut _seq1: String, mut _seq2: String) -> Vec<String> {
    _seq1 = str::replace(&_seq1, "N", "A");
    _seq1 = str::replace(&_seq1, "K", "G");
    _seq1 = str::replace(&_seq1, "R", "A");
    _seq1 = str::replace(&_seq1, "Y", "T");
    _seq1 = str::replace(&_seq1, "M", "A");
    _seq1 = str::replace(&_seq1, "S", "G");
    _seq1 = str::replace(&_seq1, "W", "A");
    _seq1 = str::replace(&_seq1, "B", "G");
    _seq1 = str::replace(&_seq1, "D", "A");
    _seq1 = str::replace(&_seq1, "H", "A");
    _seq1 = str::replace(&_seq1, "V", "A");

    _seq2 = str::replace(&_seq2, "N", "A");
    _seq2 = str::replace(&_seq2, "K", "G");
    _seq2 = str::replace(&_seq2, "R", "A");
    _seq2 = str::replace(&_seq2, "Y", "T");
    _seq2 = str::replace(&_seq2, "M", "A");
    _seq2 = str::replace(&_seq2, "S", "G");
    _seq2 = str::replace(&_seq2, "W", "A");
    _seq2 = str::replace(&_seq2, "B", "G");
    _seq2 = str::replace(&_seq2, "D", "A");
    _seq2 = str::replace(&_seq2, "H", "A");
    _seq2 = str::replace(&_seq2, "V", "A");

    let mut result: Vec<String> = Vec::new();
    result.push(_seq1);
    result.push(_seq2);
    result
}

fn score(_mat: Matrix<isize>) -> f64 {
    let length1 = _mat.rows();
    let length2 = _mat.cols();
    let max = cmp::(length1, length2);

    let mut score = _mat.get(length1, length2);
    //Modificar la puntuación

    score += max as i32;
    let mut new_score = (score as f64 / (length * 2) as f64) * 100.0;
    new_score = 100.0 - new_score;

    new_score
}
