---
records:
    - id: XJM33K2T9Y
      kind: problem-set
      title: Kvant 1976, no. 6
      date: "1976"
      expressions:
        - key: e1
          kind: edition
          date: "1976"
          structure: XJM33K2T9Y/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1976-6
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: XJMJTP4W25
      kind: monograph
      title: The Computational Complexity of Logical Theories
      creators:
        - name: Jeanne Ferrante
          role: author
        - name: Charles W. Rackoff
          role: author
      date: "1979"
      msc:
        - code: 03D15
          from: zbmath_search
        - code: 03B25
          from: zbmath_search
        - code: 03D10
          from: zbmath_search
        - code: 03-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1979"
          ids:
            doi: 10.1007/bfb0062837
            zbl: "0404.03028"
            zbl_id: "3627150"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1979"
              ids:
                isbn:
                    - "9783540095019"
                    - "9783540351979"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0062837
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3627150"
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
