---
records:
    - id: FK058VZ39B
      kind: monograph
      title: Variational Analysis and Generalized Differentiation II
      creators:
        - name: Boris S. Mordukhovich
          role: author
      date: "2006"
      msc:
        - code: 49-02
          from: zbmath_search
        - code: 49J52
          from: zbmath_search
        - code: 49J53
          from: zbmath_search
        - code: 49K27
          from: zbmath_search
        - code: 49K40
          from: zbmath_search
        - code: 90C31
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2006"
          ids:
            doi:
                - 10.1007/3-540-31246-3
                - 10.1007/3-540-31247-1
            zbl: "1100.49002"
            zbl_id: "2176481"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2006"
              ids:
                isbn:
                    - "9783540254386"
                    - "9783540312468"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2006"
              ids:
                isbn:
                    - "9783540254379"
                    - "9783540312475"
              access:
                class: record
      relations:
        - kind: part_of
          to: GQFCNY816R
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/3-540-31246-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/3-540-31247-1
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "2176481"
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
          at: "2026-11-01"
          by: m2 v0.6.14 scope/1
          note: from in to in
---
