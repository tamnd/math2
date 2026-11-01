---
records:
    - id: FP1069RB4H
      kind: monograph
      title: A Hilbert Space Problem Book
      creators:
        - name: P. R. Halmos
          role: author
      date: "1974"
      msc:
        - code: 47-02
          from: zbmath_search
        - code: 47Axx
          from: zbmath_search
        - code: 47Bxx
          from: zbmath_search
        - code: 46-02
          from: zbmath_search
        - code: 46Cxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1974"
          ids:
            doi:
                - 10.1007/978-1-4615-9976-0
                - 10.1007/978-1-4684-9330-6
            zbl: "0283.47001"
            zbl_id: "3444248"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer US
              date: "1974"
              ids:
                isbn:
                    - "9781461599784"
                    - "9781461599760"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1982"
              ids:
                isbn:
                    - "9781468493320"
                    - "9781468493306"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4615-9976-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9330-6
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3444248"
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
          by: m2 v0.6.13 scope/1
          note: from in to in
---
