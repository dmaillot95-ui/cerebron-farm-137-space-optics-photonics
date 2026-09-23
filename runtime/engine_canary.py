import json,hashlib,pathlib,platform
import math
lam=550e-9;D=2.4;theta=1.22*lam/D;arcsec=theta*206264.806;out={"wavelength_m":lam,"aperture_m":D,"rayleigh_rad":theta,"rayleigh_arcsec":arcsec};ok=0<arcsec<1
out.update({"farm":137,"engine":"python-engineering-batch-canary","engine_version":platform.python_version(),"test":"DIFFRACTION_LIMIT","status":"REAL_ENGINE_CANARY_OK" if ok else "FAIL","epistemic_status":"ENGINEERING_CANARY_NOT_PHYSICAL_VALIDATION"});raw=json.dumps(out,sort_keys=True).encode();out["result_sha256"]=hashlib.sha256(raw).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/f137_engine_canary.json").write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out));raise SystemExit(0 if ok else 1)
