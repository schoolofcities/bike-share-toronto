export function yGrids(maxY) {
    if (maxY === 0) {
        return [0];
    } else if (maxY === 1) {
        return [0, 1];
    } else if (maxY > 1 && maxY <= 40) {
        return [0, Math.floor(maxY / 2), 2 * Math.floor(maxY / 2)];
    } else if (maxY > 20 && maxY <= 400) {
        return [0, 10 * Math.floor(maxY * 0.1 / 2), 10 * 2 * Math.floor(maxY * 0.1 / 2)];
    } else if (maxY > 200 && maxY <= 4000) {
        return [0, 100 * Math.floor(maxY * 0.01 / 2), 100 * 2 * Math.floor(maxY * 0.01 / 2)];
    } else if (maxY > 2000 && maxY <= 10000) {
        console.log("meow");
        return [0, 100 * Math.floor(maxY * 0.01 / 2), 100 * 2 * Math.floor(maxY * 0.01 / 2)];
    } else {
        return [0]
    }
}