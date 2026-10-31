---
records:
    - id: J1D851YBRM
      kind: course
      title: 'Advanced Partial Differential Equations – (Part I: Distributions and Sobolev Spaces)'
      creators:
        - name: P.S. Datti
          role: instructor
        - name: A. K. Nandakumaran
          role: instructor
      ids:
        course: 04dese585:111108168
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IISc Bangalore
              ids:
                nptel: "111108168"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111108168"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
    - id: J1DKCYYYS9
      kind: monograph
      title: 'Geometry III: Theory of Surfaces'
      creators:
        - name: Yu. D. Burago
          role: editor
        - name: V. A. Zalgaller
          role: editor
      date: "1992"
      msc:
        - code: 00B50
          from: zbmath_search
        - code: 53-06
          from: zbmath_search
        - code: 53A05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1992"
          ids:
            doi: 10.1007/978-3-662-02751-6
            zbl: "0777.00060"
            zbl_id: "107903"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1992"
              ids:
                isbn:
                    - "9783642081026"
                    - "9783662027516"
              access:
                class: record
      relations:
        - kind: part_of
          to: XGZPMQ7BSM
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-02751-6
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "107903"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
