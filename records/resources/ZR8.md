---
records:
    - id: ZR8NEZ46ZW
      kind: monograph
      title: Complex Analysis
      creators:
        - name: Theodore W. Gamelin
          role: author
      date: "2001"
      msc:
        - code: 30-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2001"
          ids:
            doi: 10.1007/978-0-387-21607-2
            zbl: "0978.30001"
            zbl_id: "1520569"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2001"
              ids:
                isbn:
                    - "9780387950693"
                    - "9780387216072"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-21607-2
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "1520569"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: ZR8WFCW866
      kind: course
      title: Probability and Statistics
      creators:
        - name: Somesh Kumar
          role: instructor
      ids:
        course:
            - 03w5sq511:111105041
            - 03w5sq511:111105090
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Kharagpur
              ids:
                nptel: "111105041"
              access:
                class: record
            - key: m2
              kind: page
              publisher: IIT Kharagpur
              ids:
                nptel: "111105090"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111105041"
          level: manifestation
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111105090"
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
---
