---
records:
    - id: KY7ZWZ6GB4
      kind: monograph
      title: Smooth S1 Manifolds
      creators:
        - name: Wolf Iberkleid
          role: author
        - name: Ted Petrie
          role: author
      date: "1976"
      msc:
        - code: 57S25
          from: zbmath_search
        - code: 57-02
          from: zbmath_search
        - code: 57N65
          from: zbmath_search
        - code: 53C10
          from: zbmath_search
        - code: 57R15
          from: zbmath_search
        - code: 55N15
          from: zbmath_search
        - code: 57R20
          from: zbmath_search
        - code: 55P10
          from: zbmath_search
        - code: 57S15
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1976"
          ids:
            doi: 10.1007/bfb0091045
            zbl: "0345.57016"
            zbl_id: "3538556"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540080022"
                    - "9783540375517"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0091045
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3538556"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-02"
          by: m2 dev scope/1
          note: from in to in
---
